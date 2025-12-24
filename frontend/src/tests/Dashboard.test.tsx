import { render, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom';
import { describe, it, expect, vi } from 'vitest';
import { BrowserRouter } from 'react-router-dom';
import NodesTable from '../components/NodesTable';
import { AuthProvider } from '../context/AuthContext';

vi.mock('../api/client', () => ({
    apiClient: {
        isAuthenticated: vi.fn(() => false),
        getCurrentUser: vi.fn(),
        login: vi.fn(),
        logout: vi.fn(),
        clearToken: vi.fn(),
    },
    default: {
        isAuthenticated: vi.fn(() => false),
        getCurrentUser: vi.fn(),
        login: vi.fn(),
        logout: vi.fn(),
        clearToken: vi.fn(),
    }
}));

const renderWithProviders = (component: React.ReactNode) => {
    return render(
        <BrowserRouter>
            <AuthProvider>
                {component}
            </AuthProvider>
        </BrowserRouter>
    );
};

describe('NodesTable', () => {
    it('renders without crashing with empty data', async () => {
        const { container } = renderWithProviders(<NodesTable nodes={[]} onRefresh={vi.fn()} />);
        await waitFor(() => expect(container).toBeTruthy());
    });

    it('renders grid structure with data', async () => {
        const mockNodes = [{
            id: 'n1', node_id: 'node-001', status: 'online',
            last_heartbeat: new Date().toISOString(), node_type: 'vehicle',
            name: 'Alpha', cpu_usage: 20, memory_usage: 40, disk_usage: 10,
            registered_at: new Date().toISOString(), updated_at: new Date().toISOString(),
            description: null, latitude: null, longitude: null, altitude: null,
            ip_address: '1.2.3.4', metadata: null
        }];

        const { container } = renderWithProviders(<NodesTable nodes={mockNodes} onRefresh={vi.fn()} />);
        await waitFor(() => expect(container.firstChild).toBeTruthy());
    });
});
