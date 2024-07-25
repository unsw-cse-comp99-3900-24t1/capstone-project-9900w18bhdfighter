import React from 'react'
import { List } from 'antd'
import { Group } from '../../../types/group'

type Props = {
  item: Group
}

const GroupsAssessmentListItem: React.FC<Props> = ({ item }) => {
  return (
    <List.Item.Meta
      title={item.groupName}
      description={`Description: ${item.groupDescription}`}
    />
  )
}

export default GroupsAssessmentListItem
