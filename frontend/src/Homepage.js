import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import backgroundImage from './back_full_page.jpg';

function HomePage() {
  const [latestBlogs, setLatestBlogs] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/api/blogs/latest_blogs/')
      .then(response => response.json())
      .then(data => setLatestBlogs(data));
  }, []);

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
        <h1 style={{ fontSize: '36px', marginBottom: '20px', textAlign: 'center', color: '#30cf4b' }}>Latest Blogs</h1>
        <ul style={{ listStyle: 'none', padding: '0' }}>
          {latestBlogs.map(blog => (
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
                  style={{ fontSize: '18px', lineHeight: '1.6' }}
                  dangerouslySetInnerHTML={{ __html: blog.content }}
                ></div>
                <p style={{ color: 'gray', fontSize: '14px' }}>
                  Created at: {formatDate(blog.created_at)}
                </p>
                {blog.tags && (
                  <p>
                    <span style={{ fontWeight: 'bold' }}>Tags:</span>{' '}
                    {blog.tags.map(tag => (
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
              </div>
              {blog.thumbnail && (
                <div style={{ flex: '0 0 100px', marginLeft: '20px', alignSelf: 'flex-start' }}>
                  <img src={blog.thumbnail} alt="Blog thumbnail" style={{ width: '100%', height: 'auto', objectFit: 'cover' }} />
                </div>
              )}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default HomePage;
