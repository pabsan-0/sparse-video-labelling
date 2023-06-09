
- Video to images
- Label images by hand -> labels


START LOOP 

    - Build a temporary dataset     <- full auto
        - Fetch labelled images
        - Fetch only the images belonging to those labels

    - Train a model on that dataset   <- full auto
        - Have assets prepared to train                    -> output: trained_model
        - Add model to a registry - vX

    - Unleash your model on some/all of your data
        - define infer list                                <- Input
        - Export NEW labels                                -> output: new_labels
        - Delete redundant: some you have already labelled 
        - Label those images by hand
        - (optional) Discard newly created empty labels

    - Add the handlabelled data to the so_far labels 

    - Inspect the time-series to look for gaps
        - Hand label obvious gaps                          -> output: diagram {before net, after net, after manual}
        - Keep a history of these inspections              

    - Add the handlabelled data to the so_far labels 

END LOOP

- Save txt labels in a safe place

- Remove images to save disk
