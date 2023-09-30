import { useState, useEffect } from 'react';
import axios from 'axios';

const useFetch = (url, options) => {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [data, setdata] = useState(null);

  useEffect(() =>{
    setIsLoading(true);
    axios
      .get(url, options)
      .then((response) => {
        setIsLoading(false);
        setdata(response);
      })
      .catch((error) => {
        setIsLoading(false);
        setError(error);
      });

  }, []);

  return { isLoading, error, data };
};

export default useFetch;
