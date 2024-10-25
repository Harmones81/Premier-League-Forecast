import React from "react";
import { Link } from "react-router-dom";
import styles from "../home/Home.module.css";
import Header from "../../components/header/Header";
import playerImg from "../../images/player.png";

const Home = () =>
{
    return (
        <>
            <Header/>
            <section className={styles.headline}>
                <div className={styles.left}>
                    <h1>THE ULTIMATE FIXTURE PREDICTOR</h1>
                    <p>
                        Premier League Forecast is a free platform that you can use to help with your fixture predictions. 
                        With the help of standard Data Analysis methods, you can essentailly see the future of the Premier League.
                    </p>
                    <Link to="/">Start a Prediction</Link>
                </div>
                <img src={playerImg}/>
            </section>
        </>
    )
}

export default Home;