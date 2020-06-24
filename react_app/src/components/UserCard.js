import React from "react";
import {StyledSharpCard} from "../styles/common";
import {Link} from "react-router-dom";
import {encodeUUID} from "../utilities";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import UserAvatar from "./UserAvatar";

export default function UserCard(props) {
    return (
        <Link to={"/user/" + encodeUUID(props.user.uuid)}
              style={{textDecoration: 'none'}}>
            <StyledSharpCard style={{width: "340px", height: "100px"}}>
                <Grid container spacing={2} direction={"row"} justify={"flex-start"} alignItems={"center"}>
                    <Grid item>
                        <UserAvatar userUUID={props.user.uuid} displayName={props.user.display_name} avatarURL={props.user.avatar_url}/>
                    </Grid>
                    <Grid item>
                        <Grid container spacing={1} alignItems={"flex-start"} direction={"column"}>
                            <Grid item>
                                <Typography>{props.user.display_name}</Typography>
                            </Grid>
                            <Grid item>
                                <Typography>{props.user.patch}</Typography>
                            </Grid>
                        </Grid>
                    </Grid>
                </Grid>
            </StyledSharpCard>
        </Link>
    )
}
