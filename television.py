class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        '''
        Method to set default values of Television object
        :param self:
        '''
        self.status = False
        self.muted = False
        self.volume = Television.MIN_VOLUME
        self.channel = Television.MIN_CHANNEL

    def power(self) -> None:
        '''
        Toggles boolean in self.status to represent power state
        :param self:
        '''
        self.status = not self.status

    def mute(self) -> None:
        '''
        Toggles boolean in self.muted to represent muted state
        :param self:
        '''
        if self.status:
            self.muted = not self.muted

    def channel_up(self) -> None:
        '''
        Increases self.channel if it is within acceptable range
        :param self:
        '''
        if self.status:
            if self.channel == Television.MAX_CHANNEL:
                self.channel = Television.MIN_CHANNEL
            else:
                self.channel += 1

    def channel_down(self) -> None:
        '''
        Decreases self.channel if it is within acceptable range
        :param self:
        '''
        if self.status:
            if self.channel == Television.MIN_CHANNEL:
                self.channel = Television.MAX_CHANNEL
            else:
                self.channel -= 1

    def volume_up(self) -> None:
        '''
        Increases self.volume if it is within acceptable range and sets self.muted false
        :param self:
        '''
        if self.status:
            self.muted = False
            if self.volume < Television.MAX_VOLUME:
                self.volume += 1

    def volume_down(self) -> None:
        '''
        Decreases self.volume if it is within acceptable range and sets self.muted false
        :param self:
        '''
        if self.status:
            self.muted = False
            if self.volume > Television.MIN_VOLUME:
                self.volume -= 1

    def __str__(self) -> str:
        '''
        returns variables self.status, self.channel, and self.volume in a string
        :param self:
        :return: string containing variable states
        '''
        if self.muted:
            vol = 0
        else:
            vol = self.volume
        return f'Power = {self.status}, Channel = {self.channel}, Volume = {vol}'
