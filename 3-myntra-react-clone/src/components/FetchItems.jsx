import React, { useState } from "react";
import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { fetchStatusSliceActions } from "../store/fetchStatusSlice";
import { itemsActions } from "../store/itemsSlice";
import axios from "axios";

const FetchItems = () => {
  const fetchStatus = useSelector((store) => store.fetchStatus);

  const dispatch = useDispatch();

  /*useEffect(() => {
    if (fetchStatus.fetchDone) return;
    const controller = new AbortController();
    const signal = controller.signal;
    dispatch(fetchStatusSliceActions.markFetchingStarted());

    fetch("http://localhost:8080/items", { signal })
      .then((res) => console.log(res.json))
      .then((res) => res.json())
      .then(({ items }) => {
        console.log(items);
        dispatch(fetchStatusSliceActions.markFetchDone());
        dispatch(fetchStatusSliceActions.markFetchingFinished());

        dispatch(itemsActions.addInitialItems(items));
      });
    return () => {
      controller.abort();
    };
  }, [fetchStatus]);*/

  useEffect(() => {
    if (fetchStatus.fetchDone) return;
    const controller = new AbortController();
    const signal = controller.signal;
    dispatch(fetchStatusSliceActions.markFetchingStarted());

    const fetchData = async () => {
      const result = await axios.get("http://127.0.0.1:8000/api/items");
      dispatch(fetchStatusSliceActions.markFetchDone());
      dispatch(fetchStatusSliceActions.markFetchingFinished());

      dispatch(itemsActions.addInitialItems(result.data));
      // setData(result.data);
      console.log(result.data);
    };
    fetchData();
    return () => {
      controller.abort();
    };
  }, [fetchStatus]);

  /*const [data, setData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      const result = await axios.get("http://127.0.0.1:8000/api/items");

      setData(result.data);
      console.log(result.data);
    };
    fetchData();
  }, []);*/

  return <></>;
};

export default FetchItems;
