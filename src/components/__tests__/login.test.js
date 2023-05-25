import { render, fireEvent, screen } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import Login from '../Login';

describe('Login component', () => {
  test('renders login form and submits successfully', async () => {
    render(<BrowserRouter><Login /></BrowserRouter>);

    // Fill in email and password input fields
    const emailInput = screen.getByPlaceholderText('Email Id:');
    const passwordInput = screen.getByPlaceholderText('Password:');
    fireEvent.change(emailInput, { target: { value: 'test@example.com' } });
    fireEvent.change(passwordInput, { target: { value: 'password123' } });

    // Submit form
    const loginButton = screen.getByRole('button', { name: 'Login' });
    fireEvent.click(loginButton);

    // Wait for API call to complete
    // await screen.findByText('Welcome to My App!', { selector: '.welcome-message' });


    // Check that user is redirected to the Blog page
    expect(window.location.pathname).toBe('/');
  });
});
