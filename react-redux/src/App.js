import {useSelector, useDispatch} from 'react-redux';

import './App.css';

function App() {
  const selector = useSelector((state)=>state.counter)
  const dispatch = useDispatch()
  const increment =() =>{
    dispatch({type:"INC",payload :"hello" })
  }
  const decrement =() =>{
    dispatch({type:"DEC",payload :"hiii" })
  }
  return (
    <div className="App">
      <h1>Counter</h1>
     
      {selector}
      <button onClick={increment}>Increment</button>
      <button onClick={decrement}>Decrement</button>
    </div>
  );
}

export default App;
