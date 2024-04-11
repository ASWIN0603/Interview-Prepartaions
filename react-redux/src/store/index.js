import { createStore } from 'redux';
import { persistStore, persistReducer } from 'redux-persist';
import storage from 'redux-persist/lib/storage';

// Define your initial state
const initialState = {
  counter: 10
};

// Define your reducer function
const reducer = (state = initialState, action) => {
  if (action.type === "INC") {
    return { counter: action.payload };
  }
  if (action.type === "DEC") {
    return { counter: action.payload };
  }
  return state;
};

// Define your Redux Persist configuration
const persistConfig = {
  key: 'root',
  storage
};

// Create a persisted reducer
const persistedReducer = persistReducer(persistConfig, reducer);

// Create your Redux store with the persisted reducer
const store = createStore(persistedReducer);

// Create a persistor object to persist the store
export const persistor = persistStore(store);

export default store;
