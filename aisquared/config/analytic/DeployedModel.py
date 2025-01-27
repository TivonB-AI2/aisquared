from aisquared.base import BaseObject


class DeployedModel(BaseObject):
    """
    Interaction with a remote model

    Example usage:

    >>> import aisquared
    >>> analytic = aisquared.config.analytic.DeployedModel(
        'model_url',
        'text'
    )
    >>> analytic.to_dict()
    {'className': 'DeployedModel',
    'params': {'url': 'model_url',
    'inputType': 'text',
    'secret': 'request',
    'header': None}}

    """

    def __init__(
        self,
        url: str,
        input_type: str,
        secret: str = 'request',
        header: dict = None
    ):
        """
        Parameters
        ----------
        url : str
            The base URL for the remote endpoint
        input_type : str
            The input type to the model. Either one of 'cv', 'text', or 'tabular'
        secret : str (default 'request')
            The secret key used to interact with the service. Default value of 'request'
            indicates that the user inputs the key whenever the analytic is started again
        header : dict or None (default None)
            Header to use when calling the endpoint
        """
        super().__init__()
        self.url = url
        self.input_type = input_type
        self.secret = secret
        self.header = header

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    @property
    def input_type(self):
        return self._input_type

    @input_type.setter
    def input_type(self, value):
        self._input_type = value

    @property
    def secret(self):
        return self._secret

    @secret.setter
    def secret(self, value):
        self._secret = value

    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, value):
        self._header = value

    def to_dict(self) -> dict:
        """
        Get the config object as a dictionary
        """
        return {
            'className': 'DeployedModel',
            'params': {
                'url': self.url,
                'inputType': self.input_type,
                'secret': self.secret,
                'header': self.header
            }
        }
