// Notifications.js
import React, { useState } from 'react';
import styles from './module.css';

const Notifications = () => {
  const [showNotification, setShowNotification] = useState(true);

  const toggleNotification = () => {
    setShowNotification(!showNotification);
  };

  return (
    <div className={`notification ${showNotification ? styles.show : ''}`}>
      <button className="btn btn-primary" onClick={toggleNotification}>
        Toggle Notification
      </button>
      <div className="notification-content">
        <p>This is your notification content.</p>
      </div>
    </div>
  );
};

export default Notifications;
