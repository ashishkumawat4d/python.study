import React from 'react';
import Welcome from './Welcome';  // Import the welcome component

function App()  {
  return (
    <div>
      <Welcome name="Alice" />
      <Welcome name="Bob" />
      <Welcome name="Charlie" />
    </div>
  );
}


export default App;