import React from 'react';
import '../App.css';
import 'typeface-roboto'
import Card from '@material-ui/core/Card';
import Container from "@material-ui/core/Container";
import {styled} from '@material-ui/styles';

import {makeStyles} from '@material-ui/core/styles';
import {Paper} from "@material-ui/core";
import Box from "@material-ui/core/Box";
import {Link} from "react-router-dom"
import IconButton from "@material-ui/core/IconButton";
import ClearIcon from "@material-ui/icons/Clear";

export function DismissButton (props) {
    return (
        <IconButton
            color="inherit"
            aria-controls="simple-menu"
            aria-haspopup="true"
            size="small"
            onClick={props.onClick}>
            <ClearIcon/>
        </IconButton>
    )
}


export function MainWindowContainer(props) {
    const styles = makeStyles({
        root: {
            paddingLeft: 30,
            paddingTop: 100,
            paddingRight: 30,
            paddingBottom: "100%",
            background: "rgb(230, 230, 230)",
            align: "left",
            width: "100%",
            height: "100%"
        },
        content: {
            maxWidth: "1920px",
            height: "100%"
        }
    });
    const classes = styles();
    return (
        <div className={classes.root}>
            <div className={classes.content}>
                {props.children}
            </div>
        </div>
    )
}

export const StyledTextLink = styled(Link) ({
    a: {
        "&:hover": {
            background: "red"
        }
    },
    textDecoration: "none"
});

export const StyledColumn = styled(Box)({
    border: 0,
    boxShadow: '0 4px 6px 3px rgba(100, 100, 100, .3)',
    height: "100%",
    background: "rgba(255, 255, 255, 0.8)",
    padding: "20px"
});


export const StyledCard = styled(Card)({
    background: "rgb(252, 252, 252)",
    border: 0,
    borderRadius: 10,
    boxShadow: '0 3px 5px 2px #7a7a7a',
    color: 'black',
    padding: '20px',
    height: '250px',
    width: '300px',
});

export const StyledSharpCard = styled(Card)({
    background: "rgb(252, 252, 252)",
    border: 0,
    borderRadius: 2,
    boxShadow: '0 3px 5px 2px #7a7a7a',
    color: 'black',
    padding: '20px',
    height: '250px',
    width: '300px',
});

export const StyledStrip = styled(Card)({
    background: "rgb(250, 248, 248)",
    color: 'black',
    borderRadius: 0,
    padding: '0px',
    height: '50px',
    width: '1200px',
    cursor: "pointer"
});

export function PaddedPaper(props) {
    const padding = props.padding ? props.padding : "30px";
    const maxWidth = props.maxWidth ? props.maxWidth : "1000px";
    return (
        <Paper style={{width: props.width ? props.width : "100%", maxWidth: maxWidth, padding: padding}}>
            {props.children}
        </Paper>
    )
}
