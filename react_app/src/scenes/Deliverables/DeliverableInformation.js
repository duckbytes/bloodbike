import React, {useEffect} from "react";
import Grid from "@material-ui/core/Grid";
import DialogContentText from '@material-ui/core/DialogContentText';
import {useDispatch, useSelector} from "react-redux";
import {getDeliverables} from "../../redux/deliverables/DeliverablesActions";


export default function DeliverableInformation(props) {
    const dispatch = useDispatch();
    const deliverables = useSelector(state => state.deliverables.deliverables);
    function componentDidMount() {
        dispatch(getDeliverables(props.taskUUID));

    }

    useEffect(componentDidMount, []);

    return (
        <Grid container
              spacing={0}
              direction={"column"}
              justify={"flex-start"}
              alignItems={"center"}
        >
            {deliverables.map(deliverable => {
                return <><Grid item>
                    <DialogContentText>
                        {deliverable.type ? deliverable.type : "Unknown deliverable type."}
                    </DialogContentText>
                </Grid></>

            })
            }
        </Grid>
    )
}
