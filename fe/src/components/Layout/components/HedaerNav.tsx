<<<<<<< HEAD
import { Badge, Button, Dropdown, Flex, Popover, Tabs } from 'antd'
import type { MenuProps, TabsProps } from 'antd'
=======
import { Badge, Button, Flex, Popover, Tabs } from 'antd'
import type { TabsProps } from 'antd'
>>>>>>> 611021aaf88104bacc9b8f80151c444a7c13fb19
import { Header } from 'antd/es/layout/layout'
import styled from 'styled-components'
import { getThemeColor } from '../../../utils/styles'
import route from '../../../constant/route'
<<<<<<< HEAD
import { Link, useNavigate } from 'react-router-dom'
import { useAuthContext } from '../../../context/AuthContext'
import { IoIosNotifications } from 'react-icons/io'
import Avatar from '../../Avatar'
import LinkButton from '../../LinkButton'
=======

import { IoIosNotifications } from 'react-icons/io'

import LinkButton from '../../LinkButton'
import AvatarDropdown from './AvatarDropdown'
>>>>>>> 611021aaf88104bacc9b8f80151c444a7c13fb19

const Wrapper = styled(Header)`
  display: flex;
  justify-content: space-between;
  align-items: center;
`

const Logo = styled(LinkButton)`
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  border: none;
  font-weight: bold;
  color: ${getThemeColor('primary')};
`

const OperationsGroup = styled(Flex)`
  align-items: center;
`

const HeaderNav = () => {
<<<<<<< HEAD
  const { usrInfo } = useAuthContext()

  const { firstName, lastName, email } = usrInfo || {
    firstName: '',
    lastName: '',
    email: '',
  }

  const { logout } = useAuthContext()
  const navigate = useNavigate()

  const items: MenuProps['items'] = [
=======
  const tabItems: TabsProps['items'] = [
>>>>>>> 611021aaf88104bacc9b8f80151c444a7c13fb19
    {
      key: '1',
      label: 'Tab 1',
      children: 'Content of Tab Pane 1',
    },
    {
      key: '2',
      label: 'Tab 2',
      children: 'Content of Tab Pane 2',
    },
    {
      key: '3',
      label: 'Tab 3',
      children: 'Content of Tab Pane 3',
    },
  ]
  const tabItems: TabsProps['items'] = [
    {
      key: '1',
      label: 'Tab 1',
      children: 'Content of Tab Pane 1',
    },
    {
      key: '2',
      label: 'Tab 2',
      children: 'Content of Tab Pane 2',
    },
    {
      key: '3',
      label: 'Tab 3',
      children: 'Content of Tab Pane 3',
    },
  ]
  return (
    <Wrapper>
      <Logo to={route.DASHBOARD}>LOGO</Logo>
      <OperationsGroup>
        <Popover
          content={<Tabs defaultActiveKey="1" items={tabItems} />}
          title="Notification"
          trigger="click"
        >
          <Button
            style={{
              marginRight: '1rem',
            }}
            shape="circle"
            type="text"
          >
            <Badge size="small" dot={true}>
              <IoIosNotifications size={'1.5rem'} />
            </Badge>
          </Button>
        </Popover>
<<<<<<< HEAD
        <Dropdown placement="topLeft" menu={{ items }} trigger={['hover']}>
          <Avatar
            firstName={firstName}
            lastName={lastName}
            emailForHashToColor={email}
          />
        </Dropdown>
=======
        <AvatarDropdown />
>>>>>>> 611021aaf88104bacc9b8f80151c444a7c13fb19
      </OperationsGroup>
    </Wrapper>
  )
}

export default HeaderNav
