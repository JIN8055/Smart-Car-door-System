import React, { useState, useEffect } from 'react';
import { View, Text, Button } from 'react-native';

const App = () => {
  const [lockStatus, setLockStatus] = useState("locked");

  const toggleLock = async () => {
    const response = await fetch(`http://backend-url/${lockStatus === "locked" ? "unlock" : "lock"}`, {
      method: 'POST',
    });
    const data = await response.json();
    setLockStatus(data.status);
  };

  return (
    <View>
      <Text>Car is currently {lockStatus}</Text>
      <Button title={`Toggle Lock`} onPress={toggleLock} />
    </View>
  );
};

export default App;
