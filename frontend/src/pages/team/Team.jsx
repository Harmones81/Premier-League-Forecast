import { useEffect, useState } from "react";
import Header from "../../components/header/Header";
import Banner from "../../components/banner/Banner";
import getLogo from "../../utils/helpers/GetLogo";
import getTeamAlias from "../../utils/helpers/GetTeamAlias";
import "../team/Team.css";
import { Link } from "react-router-dom";
import { IconContext } from "react-icons/lib";
import { IoLocationOutline } from "react-icons/io5";

export default function Team()
{
    return (
        <>
            <Header/>
        </>
    )
};