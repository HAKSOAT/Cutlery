import mock
import pytest

# Create your tests here.

@pytest.mark.urls('cutlery.urls')
@pytest.mark.django_db
def test_generate_url(client):
    link = 'http://test_link.com'
    alias = 'alias'
    generated_link = 'testserver/alias'

    with mock.patch('cutlery.views.generate_alias') as generate_alias:
        generate_alias.return_value = alias

        response = client.post('/generate-random-url/', {'link': link})

    data = response.data

    expected_data = {
        'link': link,
        'alias': alias,
        'generated_link': generated_link
    }

    assert data == expected_data


@pytest.mark.urls('cutlery.urls')
@pytest.mark.django_db
def test_generate_url_without_link_param(client):
    response = client.post('/generate-random-url/')
    data = response.data
    expected_message = 'link parameter must be provided'

    assert data[0] == expected_message


@pytest.mark.urls('cutlery.urls')
@pytest.mark.django_db
def test_generate_custom_url(client):
    link = 'http://test_link.com'
    alias = 'alias'
    generated_link = 'testserver/alias'
    response = client.post('/generate-custom-url/', {'link': link,
                                                     'alias': alias})

    data = response.data

    expected_data = {
        'link': link,
        'alias': alias,
        'generated_link': generated_link
    }

    assert data == expected_data


@pytest.mark.urls('cutlery.urls')
@pytest.mark.django_db
def test_generate_url_without_required_param(client):
    client.post('/generate-custom-url/')

    response = client.post('/generate-custom-url/')
    data = response.data
    expected_message = 'link and alias parameters must be provided'

    assert data[0] == expected_message


@pytest.mark.urls('cutlery.urls')
@pytest.mark.django_db
def test_redirect(client):
    link = 'http://test_link.com'
    alias = 'alias'
    client.post('/generate-custom-url/', {'link': link,
                                          'alias': alias})

    response = client.get('/{}'.format(alias))
    redirected_link = response.url
    expected_link = link

    assert redirected_link == expected_link


@pytest.mark.urls('cutlery.urls')
@pytest.mark.django_db
def test_redirect_without_shortened_url(client):
    alias = 'alias'
    response = client.get('/{}'.format(alias))
    status_code = response.status_code
    expected_status_code = 404

    assert status_code == expected_status_code