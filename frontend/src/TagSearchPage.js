import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import backgroundImage from './back_full_page.jpg';

const TagSearchPage = () => {
  const { tagName } = useParams();
  const [blogs, setBlogs] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(`http://localhost:8000/api/blogs-by-tag/${tagName}/`)
      .then(response => {
        if (!response.ok) {
          throw new Error('Failed to fetch.');
        }
        return response.json();
      })
      .then(data => setBlogs(data))
      .catch(error => setError(error.message));
  }, [tagName]);

  const formatDate = (dateString) => {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(dateString).toLocaleDateString(undefined, options);
  };

  return (
    <div style={{
      padding: '20px',
      backgroundImage: `url(${backgroundImage})`,
      backgroundSize: 'cover',
      backgroundPosition: 'center',
      minHeight: '100vh'
    }}>
      <div style={{ maxWidth: '800px', margin: '0 auto' }}>
        <Link to="/" style={{ textDecoration: 'none', color: '#3498db', marginBottom: '20px', display: 'inline-block' }}>
          &larr; Back to Homepage
        </Link>
        <h1 style={{ fontSize: '36px', marginBottom: '20px', textAlign: 'center', color: "#30cf4b" }}>Blogs with Tag: {tagName}</h1>
        {error && <p style={{ textAlign: 'center', color: 'red' }}>Something went wrong. Please try again later.</p>}
        {blogs && blogs.length === 0 && <p style={{ textAlign: 'center' }}>No blogs found for this tag.</p>}
        <ul style={{ listStyle: 'none', padding: '0' }}>
          {blogs && blogs.map(blog => (
            <li key={blog.id} style={{ marginBottom: '30px', backgroundColor: '#c0c0c0', borderRadius: '8px', boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)', padding: '20px', display: 'flex' }}>
              <div style={{ flex: '1' }}>
                <Link
                  to={`/blog/${blog.id}`}
                  style={{
                    textDecoration: 'none',
                    color: '#3498db',
                    fontSize: '24px',
                    marginBottom: '10px',
                    display: 'inline-block'
                  }}
                  className="blog-title-link"
                >
                  <h2>{blog.title}</h2>
                </Link>
                <div
                  style={{ fontSize: '18px', lineHeight: '1.6', marginBottom: '20px' }}
                  dangerouslySetInnerHTML={{ __html: blog.content }}
                ></div>
                <p style={{ color: 'gray', fontSize: '14px', marginBottom: '20px' }}>
                  Created at: {formatDate(blog.created_at)}
                </p>
              </div>
              {blog.thumbnail && (
                <div style={{ flex: '0 0 100px', marginLeft: '20px', alignSelf: 'flex-start' }}>
                  <img src={blog.thumbnail} alt="Blog thumbnail" style={{ width: '150px', height: '150px', objectFit: 'cover' }} />
                </div>
              )}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default TagSearchPage;
