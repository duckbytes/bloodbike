import React from "react";
import {PaddedPaper} from "../styles/common";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";

export default function NotFound(props) {
    return (
        <PaddedPaper>
            <Grid container spacing={1} direction={"column"} alignItems={"center"} justify={"center"}>
                <Grid item>
                    <Typography variant={"h4"}>
                        This page not found.
                    </Typography>
                </Grid>
                <Grid item>
                    {props.children}
                </Grid>
            </Grid>
        </PaddedPaper>
    )
}