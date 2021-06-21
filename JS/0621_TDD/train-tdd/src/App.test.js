import { render, screen, fireEvent } from '@testing-library/react';
import App from './App';

test('renders learn react link', () => {
  render(<App />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});
// test('welcom message', () => {
//   render(<App />);
//   const headingElement = screen.getByText(/welcome/i);
//   expect(headingElement).toBeInTheDocument();
// });

// it('App.js: button을 click하면 새로운 데이터가 노출된다', () => {
//   const { getByText } = render(<App />);
//   fireEvent.click(getByText('showdata'));
//   getByText('newdata');
// });
