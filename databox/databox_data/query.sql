SELECT data_sources.space_id, data_sources.type, data_source_types.key
FROM data_sources
JOIN data_source_types
	on data_sources.type = data_source_types.data_source_type_id
	and data_sources.status = 10
