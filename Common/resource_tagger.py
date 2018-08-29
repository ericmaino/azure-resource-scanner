import logging
from Common.Contracts import ResourceService

class ResourceTagger:
    def __init__(self, resource_service:ResourceService, tags:dict, overwrite=True):
        self._resource_service = resource_service
        self._tags = tags
        self._overwrite = overwrite
    
    def execute(self, resource, overwrite=None):

        # Default overwrite behavior
        if overwrite is None:
            overwrite = self._overwrite

        # Create tags dictionary on object if one isn't present already
        if 'tags' not in resource:
            resource['tags'] = dict()
        
        # Tag the resource
        tags_written = 0
        for tag_key, tag_value in self._tags.items():
            if not overwrite and tag_key in resource['tags']:
                logging.info(f"Skipped tagging {resource['id']} with tag {tag_key} since it already exists.")
                continue
            resource['tags'][tag_key] = tag_value
            tags_written += 1
        
        # Skip saving if nothing was written
        if tags_written == 0:
            return

        self._resource_service.update_resource(resource)
        logging.info(f"Wrote {tags_written} tags to {resource['id']}.")
