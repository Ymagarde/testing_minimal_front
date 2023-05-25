import React from "react";
import SearchIcon from '@mui/icons-material/Search';
import GroupIcon from '@mui/icons-material/Group';
import { Link } from "react-router-dom";
import '../css/Navbar.css';
import { useEffect, useState } from "react";
const Navbar = () => {
    var user_token = JSON.parse(localStorage.getItem('user'));
    // console.log(user_token)
    let token = user_token.access
    const [user_profile_pic, setUser_profile_pic] = useState([]);


    useEffect(() => {
        const requestOptions = {
            method: 'GET',
            redirect: 'follow',
            headers: {
                'Content-Type': 'application/json',
                Accept: 'application/json',
                Authorization:
                    'Bearer ' + token,
            },
        };

        fetch(
            'http://35.90.113.221/user_profile_pic/',

            requestOptions,
        ).then(resp => {

            resp.json().then(resp => {
                // console.log(resp);
                setUser_profile_pic(resp);
            });
        });
    }, []);


    return (
        <>
            <div className="col-lg-12  sticky-top">
                <ul style={{ listStyle: "none" }}>
                    <li><a className="nav-link" href="#"><SearchIcon className="navsearch" /></a></li>

                    <li>
                        <Link to="/Profile">
                            {user_profile_pic.map((item, i) =>
                                <div key={i}> <img className="navprofile" src={'http://35.90.113.221' + item.images} /></div>
                            )}
                        </Link>
                    </li>
                    <li><a className="nav-link" href="#"><GroupIcon className="navgroup" /></a></li>
                    <li><a className="nav-link" href="#"><img className="navflag" src="\images\us.png" /> </a></li>
                </ul>
            </div>

            {/* <div className="col-sm-12" style={{ height: 60 }}>
                <nav className="navbar navbar-expand-sm  sticky-top">
                    <ul className="navbar-nav">
                        <li className="nav-item">
                            <a className="nav-link" href="#"><SearchIcon className="navsearch" /></a>
                        </li>

                        <li className="nav-item">
                            <a className="nav-link" href="#"><img className="navflag" src="\images\us.png" /> </a>
                        </li>
                        <li className="nav-item">
                            <a className="nav-link" href="#"><GroupIcon className="navgroup" /></a>
                        </li>
                        <li className="nav-item">
                            <Link to="/Profile">
                                {user_profile_pic.map((item, i) =>
                                    <div key={i}> <img className="navprofile" src={'http://35.90.113.221' + item.images} /></div>
                                )}
                            </Link>
                        </li>
                    </ul>
                </nav>
            </div> */}
        </>
    )
}
export default Navbar;