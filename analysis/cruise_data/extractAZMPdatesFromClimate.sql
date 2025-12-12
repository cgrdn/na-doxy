SELECT
  cs.cruise_id,
  cs.latitude,
  cs.longitude,
  TO_NUMBER(TO_CHAR(cs.cruise_date, 'YYYY')) year,
  TO_NUMBER(TO_CHAR(cs.cruise_date, 'MM')) month,
  TO_NUMBER(TO_CHAR(cs.cruise_date, 'DD')) day,
  cs.cruise_time,
  cs.datatype,
  cm.pressure,
  cm.temperature,
  cm.salinity,
  cs.maximum_depth,
  cs.flag,
  cm.stn_id
FROM
    climate.stations cs,
    climate.measurements cm
WHERE
    cs.stn_id = cm.stn_id
    AND cs.longitude BETWEEN -72 AND -56
    AND cs.latitude BETWEEN 41 AND 48
    AND year > 2000
    ORDER BY
    year,
    month,
    day,
    cs.longitude

