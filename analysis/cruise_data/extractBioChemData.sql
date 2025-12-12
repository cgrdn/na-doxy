/* Extract temperature and salinity data from 1948 to 1999 */
SELECT
   mi.descriptor mission_descriptor,
   mi.protocol,
   TO_NUMBER(TO_CHAR(dh.start_date, 'YYYY')) year,
   TO_NUMBER(TO_CHAR(dh.start_date, 'MM')) month,
   TO_NUMBER(TO_CHAR(dh.start_date, 'DD')) day,
   dh.start_time time,
   ev.collector_event_id || '_' || dh.collector_sample_id sample_id,
   ev.collector_event_id,
   ev.collector_station_name,
   dh.start_lat,
   dh.start_lon,
   dh.start_depth,
   dh.end_depth,
   dh.sounding,
   dh.collector_sample_id,
   dr.parameter_name,
   dt.method,
   un.name unit,
   dt.description,
   dd.data_value,
   dd.data_qc_code
FROM
   biochem.bcdiscretedtails dd,
   biochem.bcdiscretehedrs dh,
   biochem.bcdataretrievals dr,
   biochem.bcdatatypes dt,
   biochem.bcunits un,
   biochem.bcevents ev,
   biochem.bcmissions mi
WHERE
   /* link tables */
   ev.event_seq = dh.event_seq
   AND dh.discrete_seq = dd.discrete_seq
   AND dr.data_retrieval_seq = dt.data_retrieval_seq
   AND dt.data_type_seq = dd.data_type_seq
   AND mi.mission_seq = ev.mission_seq
   AND dt.unit_seq = un.unit_seq
   /* non null data only */
   AND dd.data_value IS NOT NULL
   AND TO_NUMBER(TO_CHAR(dh.start_date, 'YYYY')) >= '2000'
   AND TO_NUMBER(TO_CHAR(dh.start_date, 'YYYY')) <= '2026'
   AND dh.start_lon BETWEEN -68.00 AND -56.00
   AND dh.start_lat BETWEEN 41.5 AND 47.0
   /* custom_sample_id filter */
   /* AND ev.collector_event_id || '_' || dh.collector_sample_id = tmp."SAMPLE_ID" */
   /* AND dh.collector_sample_id = tmp."SAMPLE_ID" */
   AND dr.parameter_name IN ('Salinity', 'Temperature', 'Chlorphyll a', 'Nitrate', 'O2')
   /* AND dt.method NOT IN ('Salinity_Sal_PSS') */
   /*ORDER BY
   dh.start_date,
   dh.start_time,
   dh.start_depth*/
