import { useEffect } from 'react';
import getLogo from '../../utils/helpers/GetLogo';
import '../table/Table.css';
import Header from '../../components/header/Header';
import Footer from '../../components/footer/Footer';

export default function Table()
{
    const [teams, setTeams] = useState([]);
    const [isLoading, setLoading] = useState(true);

    useEffect(() =>
    {
        const fetchData = async () => 
        {
            setLoading(true);

            const teamsResponse = await fetch('/api/teams');
            const teamData = await teamsResponse.json();

            setTeams(teamData);
            setLoading(false);
        }

        fetchData();
    }, []);

    function displayTable()
    {
        const elements = []

        for(let i = 0; i < teams.length; i++)
        {
            elements.push(
                <tr>
                    <td>{i + 1}</td>
                    <td><img src={import.meta.env.BASE_URL + `images/logos/${getLogo(teams[i]['Team'])}`}/></td>
                    <td>{teams[i]['MP']}</td>
                    <td>{teams[i]['W']}</td>
                    <td>{teams[i]['D']}</td>
                    <td>{teams[i]['L']}</td>
                    <td>{teams[i]['GF']}</td>
                    <td>{teams[i]['GA']}</td>
                    <td>{teams[i]['GD']}</td>
                    <td><b>{teams[i]['Pts']}</b></td>
                </tr>
            )
        }

        return elements;
    };

    if(isLoading)
    {
        return (
            <div>Loading...</div>
        )
    };

    return (
        <>
            <Header/>

            <section className="table">
                <h1>Premier League Table</h1>
                <div className="table-container">
                    <table>
                        <thead>
                            <tr>
                                <th>Position</th>
                                <th>Team</th>
                                <th>MP</th>
                                <th>W</th>
                                <th>D</th>
                                <th>L</th>
                                <th>GF</th>
                                <th>GA</th>
                                <th>GD</th>
                                <th>Pts</th>
                            </tr>
                        </thead>
                        <tbody>
                            {
                                displayTable()
                            }
                        </tbody>
                    </table>
                </div>
            </section>

            <Footer/>
        </>
    )
};