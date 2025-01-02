import { Route, Routes } from 'react-router-dom'
import SharedDataProvider from '../../utils/SharedDataContext';
import Home from './pages/home/Home';
import Table from './pages/table/Table';
import './App.css'

function App() 
{
  return (
    <>
      <SharedDataProvider>
        <Routes>
          <Route path="/" element={<Home/>}/>
          <Route path="/table" element={<Table/>}/>
        </Routes>
      </SharedDataProvider>
    </>
  )
};

export default App
