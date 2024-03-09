// StudentForm.js
import React, { useState } from 'react';
import axios from 'axios';

const StudentForm = () => {
  const [formData, setFormData] = useState({
    name: '',
    id: '',
    dept: ''
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post('/api/students', formData);
      console.log(res.data);
      // Reset form after successful submission
      setFormData({
        name: '',
        id: '',
        dept: ''
      });
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div>
      <h2>Add Student</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Name"
          name="name"
          value={formData.name}
          onChange={handleChange}
        />
        <input
          type="text"
          placeholder="ID"
          name="id"
          value={formData.id}
          onChange={handleChange}
        />
        <input
          type="text"
          placeholder="Department"
          name="dept"
          value={formData.dept}
          onChange={handleChange}
        />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default StudentForm;
