import { Route, Routes } from 'react-router-dom';
import Home from './pages/home/Home';
import Fixtures from './pages/fixtures/Fixtures';
import './App.css';

function App() 
{
  return (
    <>
      <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="/fixtures" element={<Fixtures/>}/>
      </Routes>
    </>
  )
};

export default App;
