import React, {useEffect, useState} from 'react';
import '../../App.css';
import 'typeface-roboto'
import Button from '@material-ui/core/Button'
import {useDispatch, useSelector} from "react-redux";
import {loginUser} from "../../redux/login/LoginActions";
import {withSnackbar} from 'notistack';
import {PaddedPaper} from "../../styles/common";
import Grid from "@material-ui/core/Grid";
import {TextFieldUncontrolled} from "../../components/TextFields";
import Visibility from '@material-ui/icons/Visibility';
import VisibilityOff from '@material-ui/icons/VisibilityOff';
import InputAdornment from '@material-ui/core/InputAdornment';
import IconButton from '@material-ui/core/IconButton';
import OutlinedInput from "@material-ui/core/OutlinedInput";
import InputLabel from '@material-ui/core/InputLabel';
import FormControl from '@material-ui/core/FormControl';
import {createPostingSelector} from "../../redux/selectors";
import Typography from "@material-ui/core/Typography";

function getMessage(status) {
    switch (status) {
        case 401:
            return "Failed login. Please check your details."
        case 403:
            return "Unauthorised. Please check with your organisation."
        default:
            return ""
    }
}

function Login(props) {
    const dispatch = useDispatch();
    const authStatus = useSelector(state => state.authStatus);
    const serverSettings = useSelector(state => state.serverSettings);
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    const [showPassword, setShowPassword] = useState(false)

    const postingSelector = createPostingSelector(["LOGIN"]);
    const isLoggingIn = useSelector(state => postingSelector(state));

    function handleLogin() {
        if (username && password)
            dispatch(loginUser({username, password}));
    }

    useEffect(() => {
        const message = getMessage(authStatus);
        if (message)
            props.enqueueSnackbar(getMessage(authStatus), {variant: "warning", autoHideDuration: 4000});
    }, [authStatus])

    return (
        <PaddedPaper width={"400px"} height={"400px"}>
            <Grid container spacing={1} direction={"column"} alignItems={"center"} justify={"center"}>
                <Grid item>
                    <img src={serverSettings.image_url} height={"120px"} width={"120px"} style={{objectFit: "cover"}}/>
                </Grid>
                <Grid item>
                    <Typography variant="h6">
                        {serverSettings ? serverSettings.organisation_name : ""}
                    </Typography>
                </Grid>
                <Grid item>
                    <TextFieldUncontrolled label={"username"} value={username}
                                           variant={"outlined"}
                                           disabled={isLoggingIn}
                                           onPressEnter={handleLogin}
                                           onChange={(e) => {
                                               setUsername(e.target.value)
                                           }}/>
                </Grid>
                <Grid item>
                    <FormControl variant="outlined">
                        <InputLabel htmlFor="outlined-adornment-password">Password</InputLabel>
                        <OutlinedInput
                            id="outlined-adornment-password"
                            onKeyPress={(ev) => {
                                if (ev.key === 'Enter') {
                                    handleLogin()
                                    ev.preventDefault();
                                }
                            }}
                            type={showPassword ? 'text' : 'password'}
                            value={password}
                            disabled={isLoggingIn}
                            onChange={(e) => {
                                setPassword(e.target.value)
                            }}
                            endAdornment={
                                <InputAdornment position="end">
                                    <IconButton
                                        aria-label="toggle password visibility"
                                        onClick={() => setShowPassword(!showPassword)}
                                        onMouseDown={(e) => e.preventDefault()}
                                        edge="end"
                                    >
                                        {showPassword ? <Visibility/> : <VisibilityOff/>}
                                    </IconButton>
                                </InputAdornment>
                            }
                            labelWidth={70}
                        />
                    </FormControl>
                </Grid>
                <Grid item>
                    <Button disabled={!username || !password || isLoggingIn} variant="contained" color="primary"
                            onClick={handleLogin}>
                        Login
                    </Button>
                </Grid>
            </Grid>
        </PaddedPaper>
    )

}

export default withSnackbar(Login)