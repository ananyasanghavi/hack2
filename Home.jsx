import React,{ useEffect } from 'react';
import axios from 'axios';

const Home = () => {
  useEffect(() => {
    axios.get('/start_detection').then(() => {
      console.log('Detection started');
    });
  }, []);

  return <div>Home page</div>;
};

  const stopDetection = () => {
    axios.post('http://127.0.0.1:5000/stop_detection')
      .then(response => {
        console.log(response.data.message);
      })
      .catch(error => {
        console.error('Error stopping detection:', error);
      });
  };

//   return (
//     <div>
//       <h1>Eye Drowsiness Detection</h1>
//       <button onClick={startDetection}>Start Detection</button>
//       <button onClick={stopDetection}>Stop Detection</button>
//     </div>
//   );
// }

export default Home;

