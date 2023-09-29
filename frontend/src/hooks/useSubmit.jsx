import { useState, useEffect } from 'react';
import axios from 'axios';

const useSubmit = (url, data) => {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [responseData, setResponseData] = useState(null);

  useEffect(() =>{
    setIsLoading(true);
    axios
      .post(url, data)
      .then((response) => {
        setIsLoading(false);
        setResponseData(response.data);
      })
      .catch((error) => {
        setIsLoading(false);
        setError(error);
      });

  }, [url]);

  return { isLoading, error, responseData };
};

export default useSubmit;
