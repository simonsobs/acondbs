FRAGMENT_PRODUCT = """
fragment fragmentProduct on Product {
  productId
  typeId
  type_ {
    typeId
    name
  }
  attributesUnicodeText {
    edges {
      node {
        name
        value
      }
    }
  }
  attributesDate {
    edges {
      node {
        name
        value
      }
    }
  }
  attributesDateTime {
    edges {
      node {
        name
        value
      }
    }
  }
  name
  contact
  dateProduced
  producedBy
  timePosted
  postedBy
  postingGitHubUser {
    login
  }
  timeUpdated
  updatedBy
  updatingGitHubUser {
    login
  }
  paths {
    edges {
      node {
        pathId
        path
        note
      }
    }
  }
  relations {
    edges {
      node {
        relationId
        typeId
        type_ {
          typeId
          name
        }
        otherProductId
        other {
          productId
          typeId
          type_ {
            typeId
            name
          }
          name
        }
        reverseRelationId
        reverse {
          relationId
          typeId
          type_ {
            typeId
            name
          }
        }
      }
    }
  }
  note
}
"""
