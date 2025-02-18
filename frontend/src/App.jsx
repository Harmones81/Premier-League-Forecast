import { Route, Routes } from 'react-router-dom';
import Home from './pages/home/Home';
import Fixtures from './pages/fixtures/Fixtures';
import Teams from './pages/teams/Teams';
import Team from './pages/team/Team';
import Prediction from './pages/prediction/Prediction';
import './App.css';

function App() 
{
  return (
    <>
      <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="/fixtures" element={<Fixtures/>}/>
        <Route path='/teams' element={<Teams/>}/>
        <Route path='/teams/:team' element={<Team/>}/>
        <Route path='/fixtures/:homeTeam/:awayTeam' element={<Prediction/>}/>
      </Routes>
    </>
  )
};

export default App;
