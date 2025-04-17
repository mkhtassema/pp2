DROP TABLE IF EXISTS phonebook;
CREATE TABLE phonebook (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    phone VARCHAR(20)
);

CREATE OR REPLACE FUNCTION search_phonebook(pattern TEXT)
RETURNS TABLE(id INT, first_name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.first_name, p.phone
    FROM phonebook p
    WHERE p.first_name ILIKE '%' || pattern || '%'
       OR p.phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE insert_or_update_user(_name VARCHAR, _phone VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE first_name = _name) THEN
        UPDATE phonebook SET phone = _phone WHERE first_name = _name;
    ELSE
        INSERT INTO phonebook(first_name, phone) VALUES (_name, _phone);
    END IF;
END;
$$;

CREATE OR REPLACE PROCEDURE insert_many_users(_names TEXT[], _phones TEXT[])
LANGUAGE plpgsql AS $$
DECLARE
    i INT := 1;
    invalid_data TEXT[] := '{}';
BEGIN
    WHILE i <= array_length(_names, 1) LOOP
        IF _phones[i] ~ '^87[0-9]{9}$' THEN
            CALL insert_or_update_user(_names[i], _phones[i]);
        ELSE
            invalid_data := array_append(invalid_data, _names[i] || ' - ' || _phones[i]);
        END IF;
        i := i + 1;
    END LOOP;

    IF array_length(invalid_data, 1) > 0 THEN
        RAISE NOTICE 'Invalid data: %', invalid_data;
    END IF;
END;
$$;

CREATE OR REPLACE FUNCTION query_phonebook(_limit INT, _offset INT)
RETURNS TABLE(id INT, first_name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.first_name, p.phone
    FROM phonebook p
    ORDER BY p.id
    LIMIT _limit OFFSET _offset;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE delete_user(value TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phonebook
    WHERE first_name = value OR phone = value;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_user_by_value(value TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phonebook
    WHERE first_name = value OR phone = value;

    RAISE NOTICE 'User(s) with name or phone = "%" deleted', value;
END;
$$;
