import React from "react";
import '../css/Homepage.css';
import Rotate from 'react-reveal/Rotate';
import Flip from 'react-reveal/Flip';
import Fade from 'react-reveal/Fade';
import Zoom from 'react-reveal/Zoom';
import LightSpeed from 'react-reveal/LightSpeed';
import Slide from 'react-reveal/Slide';
import { Link } from "react-router-dom";
const Homepage = () => {
    return (
        <>
            <div classnamename="container-fluid">
                <div classnamename='row'>
                    <div classnamename='col-sm-12'>

                        <div className=" sticky-top">
                            <nav className="navbar navbar-default navbar-expand-sm homepagenavbar">
                                <div className="container-fluid">

                                    <div className="navbar-header">
                                        <img src='images\logo.png ' className='homepagelogo' />
                                        <p className='MyApp' >My App</p>
                                    </div>
                                    <ul className="nav navbar-nav" style={{ float: "right" }}>
                                        <li className="nav-item item1"><a className="nav-link" href="#" >Home</a></li>

                                        <li className="nav-item item2"><a className="nav-link" href="#aboutus" >About Us</a></li>

                                        <Link className="nav-link" style={{ textDecoration: 'none' }} to="/Guest"><li className="nav-item item3">Posts</li></Link>

                                        <li className="nav-item item4"><a className="nav-link" href="#footer">Contact Us</a></li>

                                        <Link className="nav-link" style={{ textDecoration: 'none' }} to="/Login">  <li className="nav-item item5">Log In</li></Link>

                                        <Link className="nav-link" style={{ textDecoration: 'none' }} to="/Register"> <li className="nav-item item6">Sign Up</li></Link>

                                    </ul>
                                </div>
                            </nav>
                        </div>

                        <video className='homepageimage' autoPlay loop muted>
                            <source src='/images\video_AdobeExpress_AdobeExpress_AdobeExpress.mp4' type='video/mp4' />
                        </video>
                        <Zoom top duration={3000}>
                            <div className='feautered col-sm-8'>

                                <p className='feautered1'>Featured Post</p>
                                <img className='feauteredimg' src='images\2e2a49_e517229392d74f7498b1f7be7a78efee_mv2.webp' />
                                <p className='feautered2'>Dec 15 . 2 min</p>
                                <p className='feautered3'>Top Hikes In Australia</p>
                                <p className='feautered4'>Create a blog post subtitle that summarizes your<br />post in s few short,punchy sentances and entices<br />your audiance to continue reading....</p>
                                <div className='linediv'></div>
                                <p className='feautered5'>0 comments</p>
                            </div>
                        </Zoom>

                        <div className='aboutusdiv'>
                            <Fade left>
                                <p id='aboutus' className='homeaboutus'>About US</p>
                                <p className='aboutusdiscription'>There are many reasons to start a blog for personal use and<br />
                                    only a handful of strong ones for business blogging. <br />
                                    Blogging for business, projects, or anything else that might<br />
                                    bring you money has a very straightforward purpose – to rank<br />
                                    your website higher in Google SERPs, a.k.a. increase your visibility.</p>
                            </Fade>
                            <Fade right>
                                <img className='aboutimage' src='\images\blogg.jpeg' />
                            </Fade>
                        </div>

                        <p id='blog' className='homerecentpost'>Recent Posts</p>

                        <div className='homerecentpostdiv'>
                            <Rotate top left>
                                <div className='homerecentpostdiv1'>
                                    <img src='images\travel.jpeg' />
                                    <p className='homerecentpostdiv1p1' >Maxico: A Gulinary<br />Journey</p>
                                </div>
                            </Rotate>

                            <Flip top>
                                <div className='homerecentpostdiv1'>
                                    <img src='images\food.webp' />
                                    <p className='homerecentpostdiv1p1' >5 Tips For Healthy<br /> Food</p>
                                </div>
                            </Flip>

                            <Rotate top right>
                                <div className='homerecentpostdiv1'>
                                    <img src='images\office.jpeg' />
                                    <p className='homerecentpostdiv1p1' >5 Tips For Budget<br /> Offices</p>
                                </div>
                            </Rotate>

                            <Rotate top left>
                                <div className='homerecentpostdiv1'>
                                    <img src='images\fintec.jpeg' />
                                    <p className='homerecentpostdiv1p1' >The Most Amazing <br />Technology</p>
                                </div>
                            </Rotate>

                            <Flip top>
                                <div className='homerecentpostdiv1'>
                                    <img src='images\fashion.jpeg' />
                                    <p className='homerecentpostdiv1p1' >Many Fashions <br />Around The World</p>
                                </div>
                            </Flip>

                            <Rotate top right>
                                <div className='homerecentpostdiv1'>
                                    <img src='images\blockchain.png' />
                                    <p className='homerecentpostdiv1p1' >Top Hikes In<br /> Bitcoin</p>

                                </div>
                            </Rotate>
                            <LightSpeed left>
                                <div className='threecard1'>
                                    <p className='threecard1a'>"I've always found NerdWallet extremely<br />
                                        helpful when I've been looking for good<br />
                                        credit options and savings options! <br />
                                        The information is very easy to understand!"</p>
                                    <b>John W.</b>
                                </div>
                            </LightSpeed>
                            <Slide top>
                                <div className='threecard2'>
                                    <p className='threecard2a'>"I've always found NerdWallet extremely<br />
                                        helpful when I've been looking for good<br />
                                        credit options and savings options! <br />
                                        The information is very easy to understand!"</p>
                                    <b>John W.</b>
                                </div>
                            </Slide>
                            <LightSpeed right>
                                <div className='threecard3'>
                                    <p className='threecard3a'>"I've always found NerdWallet extremely<br />
                                        helpful when I've been looking for good<br />
                                        credit options and savings options! <br />
                                        The information is very easy to understand!"</p>
                                    <b>John W.</b>
                                </div>
                            </LightSpeed>
                        </div>
                        <div className='longwidth'>
                            <p><span style={{ position: 'relative', left: 40 }}>159</span><br />Number Of Blogs</p>
                            <p><span style={{ position: 'relative', right: 5 }}>646</span><br />Likes</p>
                            <p><span style={{ position: 'relative', left: 10 }}>485</span><br />Comments</p>
                            <p><span style={{ position: 'relative', left: 35 }}>645</span><br />Recommendation</p>
                        </div>
                        <div id='footer' className='footer'>
                            <p className='footer1'>My App<br />The Blogging App</p>
                            <ul className='footer2' style={{ listStyle: 'none' }}>
                                <li className="nav-item"><a className="nav-link" href="#" >Home</a></li>

                                <li className="nav-item"><a className="nav-link" href="#aboutus" >About Us</a></li>

                                <li className="nav-item"><a className="nav-link" href="#blog" >Posts</a></li>

                                <li className="nav-item"><a className="nav-link" href="#">Log In</a></li>

                                <li className="nav-item"><a className="nav-link" href="#">Sign Up</a></li>
                            </ul>
                            <p className='footer3'>Contact Us</p>
                            <p className='footer4'>Subscribe here and get the latest travel tips <br /> and my insider secrets!</p>
                            <input placeholder='Email' className='footer5' type="email" />
                            <button className='footer6'>Subscribe</button>
                            <img className='footer7' src='\images\download.jpeg' />
                            <img className='footer7' src='\images\download.png' />
                            <img className='footer7' src='\images\download (2).png' />
                            <img className='footer7' src='\images\download (1).png' />
                            <p className='footer8'>© 2023 by On the Trail. Proudly created with Wix.com</p>

                        </div>

                    </div>
                </div>
            </div>
        </>
    )
}
export default Homepage