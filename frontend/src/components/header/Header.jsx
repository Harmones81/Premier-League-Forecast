import React from "react";
import { Link } from "react-router-dom";
import styles from '../header/Header.module.css';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { library } from "@fortawesome/fontawesome-svg-core";
import { faGithub } from "@fortawesome/free-brands-svg-icons";

library.add(faGithub)

const Header = () => 
{
    return (
        <header>
            <Link to="/" className={styles.logo}>PLF</Link>
            <div className={styles.links}>
                <Link to="/overview">Home</Link>
                <Link to="/predictions">Overview</Link>
                <Link to="/about">About</Link>
            </div>
            <div className={styles.socials}>
                <Link to="https://github.com/Harmones81"><FontAwesomeIcon icon={faGithub} size="2x" inverse/></Link>
            </div>
        </header>
    );
};

export default Header;