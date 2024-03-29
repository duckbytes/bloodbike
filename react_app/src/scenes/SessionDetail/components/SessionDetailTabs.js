import React, {useEffect, useState} from 'react';
import AddCircleOutline from "@material-ui/icons/AddCircleOutline";
import PropTypes from 'prop-types';
import {makeStyles} from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import Box from '@material-ui/core/Box';
import {useDispatch, useSelector} from "react-redux";
import {createPostingSelector} from "../../../redux/selectors";
import {clearTaskContextMenuSnack, setHideDelivered, setTaskContextMenuSnack} from "../../../redux/Actions";
import Tooltip from "@material-ui/core/Tooltip";
import IconButton from "@material-ui/core/IconButton";
import ChatIcon from "@material-ui/icons/Chat";
import Grid from "@material-ui/core/Grid";
import PersistentDrawerRight from "./SideInfoSection";
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Switch from '@material-ui/core/Switch';
import AvatarGroup from "@material-ui/lab/AvatarGroup";
import Typography from "@material-ui/core/Typography";
import Avatar from "@material-ui/core/Avatar";
import UserAvatar from "../../../components/UserAvatar";
import {AddCircleButtonSmall} from "../../../components/Buttons";
import {StyledAddCircleOutlineSmall, StyledAddCircleOutlineSmallDisabled} from "../../../styles/Buttons";
import CollaboratorsSection from "./CollaboratorsSection";

export function TabPanel(props) {
    const {children, index, ...other} = props;
    const value = parseInt(props.value)

    return (
        <div
            role="tabpanel"
            hidden={value !== index}
            id={`simple-tabpanel-${index}`}
            aria-labelledby={`simple-tab-${index}`}
            {...other}
        >
            {value === index && (
                <Box p={3}>
                    {children}
                </Box>
            )}
        </div>
    );
}

TabPanel.propTypes = {
    children: PropTypes.node,
    index: PropTypes.any.isRequired,
    value: PropTypes.any.isRequired,
};

function a11yProps(index) {
    return {
        id: `simple-tab-${index}`,
        'aria-controls': `simple-tabpanel-${index}`,
    };
}

const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
        backgroundColor: "rgb(240, 240, 240)",
        maxWidth: "1850px",
    },
}));

export function SessionDetailTabs(props) {
    const classes = useStyles();
    const dispatch = useDispatch();
    const [rightSideBarOpen, setRightSideBarOpen] = useState(true);
    const snack = useSelector(state => state.taskContextMenuSnack);
    const currentSession = useSelector(state => state.session.session);
    const whoami = useSelector(state => state.whoami.user);
    const hideDelivered = useSelector(state => state.hideDelivered);
    //const [toggleHideDelivered, setToggleHideDelivered] = useState(props.hideDelivered);
    const postingSelector = createPostingSelector([
        "DELETE_TASK",
        "RESTORE_TASK",
        "UPDATE_TASK",
        "UPDATE_TASK_PICKUP_TIME",
        "UPDATE_TASK_DROPOFF_TIME",
        "UPDATE_TASK_CANCELLED_TIME",
        "UPDATE_TASK_REJECTED_TIME"]);
    const isPosting = useSelector(state => postingSelector(state));

    function dispatchSnack() {
        if (!isPosting && snack !== undefined) {
            snack.snack();
            dispatch(clearTaskContextMenuSnack())
        }
    }

    useEffect(dispatchSnack, [isPosting])

    const handleChange = (event, newValue) => {
        props.onChange(event, newValue);
    };


    return (
        <div className={classes.root}>
            <PersistentDrawerRight open={rightSideBarOpen}
                                   handleDrawerToggle={() => setRightSideBarOpen(!rightSideBarOpen)}
                                   handleDrawerClose={() => setRightSideBarOpen(false)}>
                <AppBar position="static">
                    <Grid container spacing={1} direction={"row"} justify={"space-between"} alignItems={"center"}>
                        <Grid item>
                            <Tabs value={parseInt(props.value)} onChange={handleChange}
                                  aria-label="simple tabs example">
                                <Tab label="Kanban" {...a11yProps(0)} />
                                <Tab label="Table" {...a11yProps(1)} />
                                <Tab label="Statistics" {...a11yProps(2)} />
                            </Tabs>
                        </Grid>
                        <Grid item>
                            <Grid container spacing={2} direction={"row"} justify={"flex-align"} alignItems={"center"}>
                                <Grid item>
                                    <CollaboratorsSection
                                        allowAdd={(whoami.uuid === currentSession.coordinator_uuid || whoami.roles.includes("admin"))}
                                        collaborators={currentSession.collaborators}
                                        sessionUUID={currentSession.uuid}
                                        coordinatorUUID={currentSession.coordinator_uuid}
                                    />
                                </Grid>
                                <Grid item>
                                    <FormControlLabel
                                        control={
                                            <Switch
                                                checked={props.hideDelivered}
                                                onChange={() => {
                                                    dispatch(setHideDelivered(!props.hideDelivered));
                                                    //setToggleHideDelivered(!toggleHideDelivered);
                                                }}
                                                name="hide-delivered"/>}
                                        label="Hide Delivered"
                                    />
                                </Grid>
                                <Grid item>

                                    <Tooltip title="View comments">
                                        <IconButton
                                            color="inherit"
                                            aria-label="open drawer"
                                            onClick={() => setRightSideBarOpen(!rightSideBarOpen)}
                                        >
                                            <ChatIcon/>
                                        </IconButton>
                                    </Tooltip>
                                </Grid>
                            </Grid>
                        </Grid>
                    </Grid>
                </AppBar>
                {props.children}
            </PersistentDrawerRight>
        </div>
    );
}
