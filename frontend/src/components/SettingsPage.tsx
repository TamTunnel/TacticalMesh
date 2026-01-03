// Copyright 2024 TacticalMesh Contributors
// SPDX-License-Identifier: Apache-2.0

import React, { useEffect, useState } from "react";
import {
  Box,
  Typography,
  Card,
  CardContent,
  CardHeader,
  Switch,
  FormControlLabel,
  Divider,
  Alert,
  CircularProgress,
  Stack,
  Chip,
} from "@mui/material";
import { PlayArrow, Stop, Hub } from "@mui/icons-material";
import { apiClient, SimulationStatus } from "../api/client";

const SettingsPage: React.FC = () => {
  const [loading, setLoading] = useState(true);
  const [actionLoading, setActionLoading] = useState(false);
  const [status, setStatus] = useState<SimulationStatus | null>(null);
  const [error, setError] = useState<string | null>(null);

  const fetchStatus = async () => {
    try {
      const data = await apiClient.getSimulationStatus();
      setStatus(data);
      setError(null);
    } catch (err) {
      console.error(err);
      // Ignore 403s if not admin, but we assume admin for demo
      setError("Failed to fetch simulation status");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchStatus();
    // Poll status every 5 seconds if active
    const interval = setInterval(() => {
      if (status?.active) {
        fetchStatus();
      }
    }, 5000);
    return () => clearInterval(interval);
  }, [status?.active]);

  const handleToggleSimulation = async (checked: boolean) => {
    setActionLoading(true);
    try {
      if (checked) {
        await apiClient.startSimulation();
      } else {
        await apiClient.stopSimulation();
      }
      // Wait a bit for backend to react
      setTimeout(() => {
        fetchStatus();
        setActionLoading(false);
      }, 1000);
    } catch (err) {
      console.error(err);
      setError(`Failed to ${checked ? "start" : "stop"} simulation`);
      setActionLoading(false);
    }
  };

  if (loading && !status) {
    return <CircularProgress />;
  }

  return (
    <Box maxWidth="md">
      <Typography variant="h4" fontWeight={600} gutterBottom>
        Settings
      </Typography>

      {error && (
        <Alert severity="error" sx={{ mb: 3 }}>
          {error}
        </Alert>
      )}

      <Card sx={{ mb: 3 }}>
        <CardHeader
          title="Demo Mode"
          subheader="Internal simulation engine for demonstrations"
          avatar={<Hub color="primary" />}
        />
        <Divider />
        <CardContent>
          <Box
            display="flex"
            alignItems="center"
            justifyContent="space-between"
          >
            <Box>
              <Typography variant="body1" gutterBottom>
                <strong>Live Traffic Simulation</strong>
              </Typography>
              <Typography variant="body2" color="text.secondary">
                Uses the internal engine to simulate 4 tactical nodes moving and
                generating telemetry.
                <br />
                <em>Use this for executive demos without external scripts.</em>
              </Typography>
            </Box>

            <FormControlLabel
              control={
                <Switch
                  checked={status?.active || false}
                  onChange={(e) => handleToggleSimulation(e.target.checked)}
                  disabled={actionLoading}
                  color="success"
                />
              }
              label={
                <Box display="flex" alignItems="center" gap={1}>
                  {status?.active ? (
                    <Chip
                      icon={<PlayArrow />}
                      label="RUNNING"
                      color="success"
                      size="small"
                    />
                  ) : (
                    <Chip
                      icon={<Stop />}
                      label="STOPPED"
                      color="default"
                      size="small"
                    />
                  )}
                  {actionLoading && <CircularProgress size={20} />}
                </Box>
              }
            />
          </Box>

          {status?.active && (
            <Box mt={3} p={2} bgcolor="background.default" borderRadius={1}>
              <Typography
                variant="subtitle2"
                gutterBottom
                color="text.secondary"
              >
                SIMULATION METRICS
              </Typography>
              <Stack direction="row" spacing={4}>
                <Box>
                  <Typography
                    variant="caption"
                    display="block"
                    color="text.secondary"
                  >
                    Active Nodes
                  </Typography>
                  <Typography variant="h6">
                    {status.nodes_count} / {status.simulated_nodes}
                  </Typography>
                </Box>
                <Box>
                  <Typography
                    variant="caption"
                    display="block"
                    color="text.secondary"
                  >
                    Uptime
                  </Typography>
                  <Typography variant="h6">
                    {status.start_time
                      ? new Date(status.start_time).toLocaleTimeString()
                      : "-"}
                  </Typography>
                </Box>
              </Stack>
            </Box>
          )}
        </CardContent>
      </Card>

      <Alert severity="info" variant="outlined">
        More settings (User Management, Network Config) coming soon in v0.2.0.
      </Alert>
    </Box>
  );
};

export default SettingsPage;
