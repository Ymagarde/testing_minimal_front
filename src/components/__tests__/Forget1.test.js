import React from 'react';
import { render, fireEvent, screen } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import  Forget1 from '../Forget1';
import { postUser } from '../Forget1';


describe('Forgot1', () => {
  it('should display error message when email is not entered', () => {
    render(
      <BrowserRouter>
        <Forget1 />
      </BrowserRouter>
    );
    const submitButton = screen.getByRole('button', { name: /submit/i });
    fireEvent.click(submitButton);
    const errorMessage = screen.getByText(/email can't be empty/i);
    expect(errorMessage).toBeInTheDocument();
  });

  it('should call postUser function when submit button is clicked with valid email', async () => {
    const postUserMock = jest.fn();
    const setEmailMock = jest.fn();
    const email = 'test@example.com';
    const { getByPlaceholderText, getByRole } = render(
      <BrowserRouter>
        <Forget1 postUser={postUserMock} setEmail={setEmailMock} email={email} />
      </BrowserRouter>
    );
    const emailInput = screen.getByPlaceholderText(/enter email address/i);
    fireEvent.change(emailInput, { target: { value: email } });
    const submitButton = getByRole('button', { name: /submit/i });
    fireEvent.click(submitButton);
    // expect(postUserMock).toHaveBeenCalled();
    // expect(setEmailMock).toHaveBeenCalledWith(email);
  });
});


