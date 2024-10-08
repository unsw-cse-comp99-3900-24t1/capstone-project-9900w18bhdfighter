import { Flex, Typography } from 'antd'
import styled from 'styled-components'
import { getThemeColor as c, getThemeToken as t } from '../../utils/styles'
import LinkButton from '../../components/LinkButton'
import { useNavigate } from 'react-router-dom'
import route from '../../constant/route'
import { useAuthContext } from '../../context/AuthContext'

const Wrapper = styled(Flex)`
  height: 100vh;
  background-color: ${c('basicBg')};
  padding: ${t('paddingLG', 'px')};
`
const WelcomeContainer = styled(Flex)`
  height: 100%;
  width: 70%;
  background-color: ${c('grayscalePalette', 1)};
  box-shadow: ${t('boxShadow')};
`
const AuthArea = styled(Flex)`
  position: relative;
  height: 100%;
  width: 30%;
`
const LoginButton = styled(LinkButton)`
  position: absolute;
  top: 0;
  right: 0;
`
const SignUpButton = styled(LinkButton)`
  width: 100%;
`
const Banner = styled(Flex)`
  padding: 0 ${t('paddingMD', 'px')};
  width: 100%;
  height: 50px;
  background-color: ${c('highlight')};
`

const LandingPage = () => {
  const navigate = useNavigate()
  const { haveLoggedIn } = useAuthContext()
  return (
    <Wrapper gap={'large'} justify="center" align="center">
      <WelcomeContainer justify="center">
        <Banner align="center">
          <Typography.Title level={3}>Welcome</Typography.Title>
        </Banner>
      </WelcomeContainer>
      <AuthArea justify="center" align="center">
        <LoginButton
          type="primary"
          to={'/login'}
          onClick={() => {
            haveLoggedIn() ? navigate(route.DASHBOARD) : navigate(route.LOGIN)
          }}
        >
          LogIn
        </LoginButton>
        <SignUpButton type="primary" to={'/sign-up'}>
          Create an account
        </SignUpButton>
      </AuthArea>
    </Wrapper>
  )
}

export default LandingPage
