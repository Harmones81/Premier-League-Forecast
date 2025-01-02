import React, { useState, useEffect, createContext } from "react";

const DataContext = createContext();

export default function SharedDataProvider({children})
{
    const [data, setData] = useState([]);
    const [isLoading, setLoading] = useState(true);

    useEffect(() =>
    {
        async function fetchData()
        {
            try
            {
                const teamsResponse = await fetch('/api/teams');
                const teamData = await teamsResponse.json();
                setData([...data, ...teamData]);

                const nextGameweekResponse = await fetch('/api/fixtures/gameweek/18');
                const nextGameweekData = await nextGameweekResponse.json();
                setData([...data, ...nextGameweekData]);

                const fixtureResultsResponse = await fetch('/api/fixtures/played');
                const fixtureResultsData = await fixtureResultsResponse.json();
                setData([...data, ...fixtureResultsData]);
            }
            catch(error)
            {
                console.error('Error fetching data:', error);
            }
            finally
            {
                setLoading(false);
            }
        }

        fetchData();

    }, []);

    return (
        <DataContext.Provider value={{ data, isLoading }}>
            {children}
        </DataContext.Provider>
    );
};