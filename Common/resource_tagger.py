import logging
from Common.Helpers import ResourceExtractors
from Common.Contracts import ServiceFactory

class ResourceTagger:
    def __init__(self, factory:ServiceFactory, tags:dict, overwrite=True):
        self._factory = factory
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
        tags_skipped = 0
        for tag_key, tag_value in self._tags.items():
            if not overwrite and tag_key in resource['tags']:
                logging.info(f"Skipped tagging {resource['id']} with tag {tag_key} since it already exists.")
                tags_skipped += 1
                continue
            resource['tags'][tag_key] = tag_value
            tags_written += 1
        
        # Only save if needed
        if tags_written > 0:
            subscription_id = ResourceExtractors.get_subscription(resource['id'])
            self._factory.resource_service(subscription_id).update_resource(resource)
            logging.info(f"Wrote {tags_written} tags to {resource['id']}.")

        return tags_written, tags_skipped
