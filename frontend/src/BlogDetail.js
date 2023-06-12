import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import backgroundImage from './back_full_page.jpg';

const BlogDetail = () => {
  const { id } = useParams();
  const [blog, setBlog] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(`http://localhost:8000/api/blogs/${id}/`)
      .then(response => {
        if (!response.ok) {
          throw new Error('Failed to fetch.');
        }
        return response.json();
      })
      .then(data => setBlog(data))
      .catch(error => setError(error.message));
  }, [id]);

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
      <div style={{ maxWidth: '1200px', margin: '0 auto', backgroundColor: 'rgba(240, 244, 248, 0.9)', borderRadius: '8px', boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)', padding: '40px' }}>
        <Link to="/" style={{ textDecoration: 'none', color: '#3498db', marginBottom: '20px', display: 'inline-block' }}>
          &larr; Back to Homepage
        </Link>
        {error && <p style={{ textAlign: 'center', color: 'red' }}>Something went wrong. Please try again later.</p>}
        {blog && (
          <>
            <h1 style={{ fontSize: '48px', marginBottom: '20px', textAlign: 'center', color: '#0F1A2F' }}>{blog.title}</h1>
            <div style={{ display: 'flex' }}>
              <div style={{ position: 'relative', marginRight: '20px' }}>
                {blog.full_image && (
                  <img src={blog.full_image} alt="Blog full image" style={{ width: '300px', height: '300px', objectFit: 'cover', borderRadius: '8px' }} />
                )}
              </div>
              <div style={{ fontSize: '22px', lineHeight: '1.8', color: '#333' }} dangerouslySetInnerHTML={{ __html: blog.content || '<p>No content available</p>' }}></div>
            </div>
            {blog.tags && (
              <p style={{ marginTop: '15px', fontSize: '18px' }}>
                Tags: {blog.tags.map(tag => (
                  <Link
                    key={tag.id}
                    to={`/tags/${tag.name}`}
                    style={{ marginRight: '10px', textDecoration: 'none', color: '#3498db' }}
                  >
                    {tag.name}
                  </Link>
                ))}
              </p>
            )}
            <p style={{ color: 'gray', fontSize: '16px' }}>
              Created at: {formatDate(blog.created_at)}
            </p>
          </>
        )}
      </div>
    </div>
  );
};

export default BlogDetail;
