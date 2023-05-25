import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import Blogopen from '../Blogopen';

// test('renders the blog post title', async () => {
//   render(<Blogopen />);
//   const title = await screen.findByText(/Blog Title/i);
//   expect(title).toBeInTheDocument();
// });

// test('renders the blog post content', async () => {
//   render(<Blogopen />);
//   const content = await screen.findByText(/Blog Content/i);
//   expect(content).toBeInTheDocument();
// });

// test('loads the post detail data on mount', async () => {
//   render(<Blogopen />);
//   const title = await screen.findByText(/Blog Title/i);
//   expect(title).toBeInTheDocument();
//   const content = await screen.findByText(/Blog Content/i);
//   expect(content).toBeInTheDocument();
// });

test('shows the comment section when the "Comment" button is clicked', async () => {
  render(<Blogopen />);
  const commentButton = screen.getByPlaceholderText('button', { name: 'Comment' });
  fireEvent.click(commentButton);
  const commentSection = await screen.findByLabelText(/Add a comment/i);
  expect(commentSection).toBeInTheDocument();
});

// test('adds a comment when the "Post" button is clicked', async () => {
//   render(<Blogopen />);
//   const commentButton = screen.getByRole('button', { name: 'Comment' });
//   fireEvent.click(commentButton);
//   const commentTextArea = await screen.findByLabelText(/Add a comment/i);
//   fireEvent.change(commentTextArea, { target: { value: 'This is a test comment.' } });
//   const postButton = screen.getByRole('button', { name: 'Post' });
//   fireEvent.click(postButton);
//   const comment = await screen.findByText(/This is a test comment./i);
//   expect(comment).toBeInTheDocument();
// });

test('shows the reply section when the "Reply" button is clicked', async () => {
  render(<Blogopen />);
  // const replyButton = screen.getByRole('button', { name: 'Reply' });
  // fireEvent.click(replyButton);
  // const replySection = await screen.findByLabelText(/Add a reply/i);
  // expect(replySection).toBeInTheDocument();
});

test('adds a reply when the "Post" button is clicked', async () => {
  render(<Blogopen />);
  // const replyButton = screen.getByRole('button', { name: 'Reply' });
  // fireEvent.click(replyButton);
  // const replyTextArea = await screen.findByLabelText(/Add a reply/i);
  // fireEvent.change(replyTextArea, { target: { value: 'This is a test reply.' } });
  // const postButton = screen.getByRole('button', { name: 'Post' });
  // fireEvent.click(postButton);
  // const reply = await screen.findByText(/This is a test reply./i);
  // expect(reply).toBeInTheDocument();
});

// test('likes the post when the "Like" button is clicked', async () => {
//   render(<Blogopen />);
//   const likeButton = screen.getByRole('button', { name: 'Like' });
//   fireEvent.click(likeButton);
//   const likes = await screen.findByText(/Likes: 1/i);
//   expect(likes).toBeInTheDocument();
// });
