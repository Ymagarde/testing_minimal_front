import { render, screen } from '@testing-library/react';
import App from './App';
// import { render } from '@testing-library/react';


test('header renders with react testing tutorial in the document', () => {
  render(<App />);
  const linkElement = screen.getByText(/data/i);
  expect(linkElement).toBeInTheDocument();
});


// test('renders login component in the document', () => {
//   const{ getByLabelText } = render(<App />);
//   const ChaidElement = getByLabelText("Email");
//   expect(ChaidElement).toBeInTheDocument();
// });
