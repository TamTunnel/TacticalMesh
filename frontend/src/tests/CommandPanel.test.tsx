import { render, screen, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { BrowserRouter } from 'react-router-dom';
import CommandPanel from '../components/CommandsPanel';
import { AuthProvider } from '../context/AuthContext';

// vi.mock must use inline factory - no external references
vi.mock('../api/client', () => ({
    apiClient: {
        isAuthenticated: vi.fn(() => false),
        getCurrentUser: vi.fn(),
        createCommand: vi.fn(),
        login: vi.fn(),
        logout: vi.fn(),
        clearToken: vi.fn(),
        getCommands: vi.fn(() => Promise.resolve({ commands: [], total: 0 })),
    },
    default: {
        isAuthenticated: vi.fn(() => false),
        getCurrentUser: vi.fn(),
        createCommand: vi.fn(),
        login: vi.fn(),
        logout: vi.fn(),
        clearToken: vi.fn(),
        getCommands: vi.fn(() => Promise.resolve({ commands: [], total: 0 })),
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

describe('CommandPanel', () => {
    it('renders command panel header', async () => {
        renderWithProviders(<CommandPanel nodeId="test-node-001" />);

        await waitFor(() => {
            // Look for text that should be in CommandsPanel
            const header = screen.queryByText(/command/i);
            expect(header).toBeTruthy();
        }, { timeout: 2000 });
    });
});
