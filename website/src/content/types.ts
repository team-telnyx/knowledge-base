export interface Article {
  slug: string;
  title: string;
  description: string | null;
  sourceUrl: string | null;
  scraped: string | null;
  collectionPath: string;
  body: string;
}

export interface Collection {
  path: string;
  title: string;
  description: string | null;
  sourceUrl: string | null;
  sourceSlug: string | null;
  intercomCollectionId: string | null;
  metadataStub: boolean;
  parentPath: string | null;
  childCollectionPaths: string[];
  articleSlugs: string[];
}
