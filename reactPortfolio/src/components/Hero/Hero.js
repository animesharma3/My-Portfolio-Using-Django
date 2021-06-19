import React from 'react';

import { Section, SectionText, SectionTitle } from '../../styles/GlobalComponents';
import Button from '../../styles/GlobalComponents/Button';
import { LeftSection } from './HeroStyles';

const Hero = (props) => (
  <Section row nopadding>
    <LeftSection>
      <SectionTitle main center>
        Welcome to <br />
        My Personal Portfolio
      </SectionTitle>
      <SectionText>
        I am passionate about using data and common sense to generate simple and implementable solution to complex problems. Decision making is becoming quantitative, reason why I am getting obsessed with keeping myself updated with newest technologies, trends, tools, algorithms and analytical techniques.
      </SectionText>
      <Button onclick={() => window.location = 'https://google.com'}>Learn More</Button>
    </LeftSection>
  </Section>
);

export default Hero;