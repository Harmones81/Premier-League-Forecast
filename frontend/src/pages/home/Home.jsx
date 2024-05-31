import React from "react";
import { Link } from "react-router-dom";
import styles from "../home/Home.module.css";
import Header from "../../components/header/Header";
import playersImg from "../../assets/player.png";

const Home = () => 
{
    return (
        <>
            <Header/>
            <section className={styles.headline}>
                <div className={styles.left}>
                    <h1>THE ULTIMATE PREMIER LEAGUE ASSISTANT</h1>
                    <p>
                        Premier League Forecast is a free platform that you can use to help with any of your Premier League neeeds. Whether it's FPL predictions or a look ahead into future matchups, we have everything you could ask for.
                    </p>
                    <Link to="/predictions">Start a Prediction</Link>
                </div>
                <img src={playersImg}/>
            </section>
        </>
    );
};

export default Home;