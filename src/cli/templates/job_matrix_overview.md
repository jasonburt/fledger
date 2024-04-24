This is the **Job Assessment Matrix**.
You can make notes outside of the table and you can also make notes in the table in the **notes** column.
The **example** section is updated by running a search request to create a record, and then an update command.

If the table is emtpy, then the terms provided did not match any requirement descriptions in the given Standards Set. 
Try modifying the set of terms, or try passing in a different Standards Set.

```sh
fledger search 'README*' --search-type=file --save=user
```

```sh
fledger update-job-assesment
```
